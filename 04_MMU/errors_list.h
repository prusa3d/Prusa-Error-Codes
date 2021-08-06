// errors_list.h
// Intended as a list of MMU errors for the Buddy FW, therefore the structure
// of this file is similar as in 12_MINI
#pragma once
#include "inttypes.h"
#include "i18n.h"

static constexpr uint8_t ERR_MMU_CODE = 4;

typedef enum : uint16_t {
    ERR_UNDEF = 0,

    ERR_MECHANICAL = 100,
    ERR_MECHANICAL_FINDA_DIDNT_SWITCH_ON,
    ERR_MECHANICAL_FINDA_DIDNT_SWITCH_OFF,
    ERR_MECHANICAL_FSENSOR_DIDNT_SWITCH_ON,
    ERR_MECHANICAL_FSENSOR_DIDNT_SWITCH_OFF,

    ERR_TEMPERATURE = 200,
    ERR_TEMPERATURE_TMC_OVER_TEMPERATURE_WARN,
    ERR_TEMPERATURE_TMC_OVER_TEMPERATURE_ERROR,

    ERR_ELECTRO = 300,
    ERR_ELECTRO_TMC_IOIN_MISMATCH,
    ERR_ELECTRO_TMC_RESET,
    ERR_ELECTRO_TMC_UNDERVOLTAGE_ON_CHARGE_PUMP,
    ERR_ELECTRO_TMC_SHORT_TO_GROUND,

    ERR_CONNECT = 400,
    ERR_CONNECT_MMU_NOT_RESPONDING,

    ERR_SYSTEM = 500,
    ERR_SYSTEM_FILAMENT_ALREADY_LOADED,
    ERR_SYSTEM_INTERNAL,

    ERR_OTHER = 900
} err_num_t;

typedef struct {
    // 32 bit
    const char *err_title;
    const char *err_text;
    // 16 bit
    err_num_t err_num;
} err_t;

static constexpr err_t error_list[] = {
    // r=1, c=19
    { N_("FINDA DIDNT SWITCH ON"),
        // r=5, c=20
        N_(""),
        ERR_MECHANICAL_FINDA_DIDNT_SWITCH_ON },

    // r=1, c=19
    { N_("FINDA DIDNT SWITCH OFF"),
        // r=5, c=20
        N_(""),
        ERR_MECHANICAL_FINDA_DIDNT_SWITCH_OFF },

    // r=1, c=19
    { N_(""),
        // r=5, c=20
        N_("FSENSOR DIDNT SWITCH ON"),
        ERR_MECHANICAL_FSENSOR_DIDNT_SWITCH_ON },

    // r=1, c=19
    { N_("FSENSOR DIDNT SWITCH OFF"),
        // r=5, c=20
        N_(""),
        ERR_MECHANICAL_FSENSOR_DIDNT_SWITCH_OFF },

    // r=1, c=19
    { N_("TMC OVER TEMPERATURE WARN"),
        // r=5, c=20
        N_(""),
        ERR_TEMPERATURE_TMC_OVER_TEMPERATURE_WARN },

    // r=1, c=19
    { N_(""),
        // r=5, c=20
        N_("TMC OVER TEMPERATURE ERROR"),
        ERR_TEMPERATURE_TMC_OVER_TEMPERATURE_ERROR },

    // r=1, c=19
    { N_("TMC IOIN MISMATCH"),
        // r=5, c=20
        N_(""),
        ERR_ELECTRO_TMC_IOIN_MISMATCH },

    // r=1, c=19
    { N_("TMC RESET"),
        // r=5, c=20
        N_(""),
        ERR_ELECTRO_TMC_RESET },

    // r=1, c=19
    { N_("TMC UNDERVOLTAGE ON CHARGE PUMP"),
        // r=5, c=20
        N_(""),
        ERR_ELECTRO_TMC_UNDERVOLTAGE_ON_CHARGE_PUMP },

    // r=1, c=19
    { N_("TMC SHORT TO GROUND"),
        // r=5, c=20
        N_(""),
        ERR_ELECTRO_TMC_SHORT_TO_GROUND },

    // r=1, c=19
    { N_("MMU NOT RESPONDING"),
        // r=5, c=20
        N_(""),
        ERR_CONNECT_MMU_NOT_RESPONDING },

    // r=1, c=19
    { N_("FILAMENT ALREADY LOADED"),
        // r=5, c=20
        N_(""),
        ERR_SYSTEM_FILAMENT_ALREADY_LOADED },

    // r=1, c=19
    { N_("INTERNAL"),
        // r=5, c=20
        N_(""),
        ERR_SYSTEM_INTERNAL }
};
