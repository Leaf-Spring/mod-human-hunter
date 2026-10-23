#!/usr/bin/env python3
import struct
import os

HUNTER_CLASS_BIT = 4     # Bit para Cazador (2^(3-1) = 4)
HUMAN_RACE_BIT = 1       # Bit para Humano (2^(1-1) = 1)

# ID de hechizo para la habilidad racial activa del Humano: Every Man for Himself (20597)
TARGET_RACIAL_SPELLS = {}

def patch_char_base_info(filename="CharBaseInfo.dbc", race=1, class_id=3):
    print("=== 1/3: Procesando CharBaseInfo.dbc ===")
    if not os.path.exists(filename):
        print(f"[!] Archivo no encontrado: {filename}\n")
        return

    with open(filename, "rb") as f:
        data = bytearray(f.read())

    magic, record_count, field_count, record_size, string_block_size = struct.unpack("<4sIIII", data[:20])
    records_start = 20
    string_block_start = records_start + (record_count * record_size)

    # Verificar si la combinación Humano (1) - Cazador (3) ya existe
    for i in range(record_count):
        off = records_start + (i * record_size)
        r, c = data[off], data[off + 1]
        if r == race and c == class_id:
            print(f"[-] OMITIDO: La combinación Humano ({race}) - Cazador ({class_id}) ya existe en el archivo.\n")
            return

    new_record = bytes([race, class_id])
    data[string_block_start:string_block_start] = new_record
    struct.pack_into("<I", data, 4, record_count + 1)

    with open(filename, "wb") as f:
        f.write(data)
    print(f"[+] ÉXITO: Se registró la combinación Humano ({race}) + Cazador ({class_id}).\n")


def patch_char_start_outfit(filename="CharStartOutfit.dbc", target_race=1, target_class=3, source_race=4):
    print("=== 2/3: Procesando CharStartOutfit.dbc ===")
    if not os.path.exists(filename):
        print(f"[!] Archivo no encontrado: {filename}\n")
        return

    with open(filename, "rb") as f:
        data = bytearray(f.read())

    magic, record_count, field_count, record_size, string_block_size = struct.unpack("<4sIIII", data[:20])
    records_start = 20
    string_block_start = records_start + (record_count * record_size)

    max_id = 0
    already_exists = False
    templates = []

    # Clonamos los outfits de inicio de Cazador Elfo de la Noche (Raza 4, Clase 3)
    for i in range(record_count):
        off = records_start + (i * record_size)
        outfit_id = struct.unpack_from("<I", data, off)[0]
        race = data[off + 4]
        cls = data[off + 5]

        if outfit_id > max_id:
            max_id = outfit_id

        if race == target_race and cls == target_class:
            already_exists = True

        if race == source_race and cls == target_class:
            templates.append(bytearray(data[off : off + record_size]))

    if already_exists:
        print(f"[-] OMITIDO: Los outfits para Humano ({target_race}) - Cazador ({target_class}) ya existen.\n")
        return

    if not templates:
        print(f"[!] ERROR: No se encontraron las plantillas de Cazador Elfo de la Noche (Raza {source_race}).\n")
        return

    added_bytes = bytearray()
    added_count = 0

    for template in templates:
        max_id += 1
        cloned = bytearray(template)
        struct.pack_into("<I", cloned, 0, max_id)
        cloned[4] = target_race                   # Raza Humano (1)
        
        added_bytes.extend(cloned)
        added_count += 1

    data[string_block_start:string_block_start] = added_bytes
    struct.pack_into("<I", data, 4, record_count + added_count)

    with open(filename, "wb") as f:
        f.write(data)
    print(f"[+] ÉXITO: Se clonaron {added_count} outfits para Humano Cazador.\n")


def patch_skill_line_ability(filename="SkillLineAbility.dbc"):
    print("=== 3/3: Procesando SkillLineAbility.dbc ===")
    if not os.path.exists(filename):
        print(f"[!] Archivo no encontrado: {filename}\n")
        return

    with open(filename, "rb") as f:
        data = bytearray(f.read())

    magic, record_count, field_count, record_size, string_block_size = struct.unpack("<4sIIII", data[:20])
    records_start = 20

    patched_spells = 0

    for i in range(record_count):
        off = records_start + (i * record_size)
        
        spell_id = struct.unpack_from("<I", data, off + 8)[0]
        race_mask = struct.unpack_from("<I", data, off + 12)[0]
        class_mask = struct.unpack_from("<I", data, off + 16)[0]

        if (race_mask & HUMAN_RACE_BIT) and (spell_id in TARGET_RACIAL_SPELLS):
            if class_mask != 0 and not (class_mask & HUNTER_CLASS_BIT):
                new_class_mask = class_mask | HUNTER_CLASS_BIT
                struct.pack_into("<I", data, off + 16, new_class_mask)
                patched_spells += 1
                print(f"[+] Hechizo {spell_id}: ClassMask {class_mask} -> {new_class_mask}")

    if patched_spells > 0:
        with open(filename, "wb") as f:
            f.write(data)
        print(f"\n[+] ÉXITO: Se actualizó el ClassMask en {patched_spells} hechizos raciales.\n")
    else:
        print("[-] OMITIDO: Las raciales activas ya son globales (ClassMask 0) o están configuradas correctamente.\n")


if __name__ == "__main__":
    print("=== APLICANDO PARCHES BINARIOS A DBCs (HUMANO CAZADOR) ===\n")
    patch_char_base_info()
    patch_char_start_outfit()
    patch_skill_line_ability()
    print("=== PROCESO COMPLETADO ===")