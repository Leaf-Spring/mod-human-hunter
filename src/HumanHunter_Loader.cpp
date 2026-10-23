#include "ScriptMgr.h"

// Clase base vacía para registrar el módulo en el emulador
class mod_human_hunter : public PlayerScript {
public:
    mod_human_hunter() : PlayerScript("mod_human_hunter") {}
};

// Función de carga requerida por AzerothCore
void Addmod_human_hunterScripts() {
    new mod_human_hunter();
}