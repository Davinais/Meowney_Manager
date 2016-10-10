async def calcext(extobj, extatk, extdef, extmatk, extmdef):
    extobj["ATK"] += extatk
    extobj["DEF"] += extdef
    extobj["MATK"] += extmatk
    extobj["MDEF"] += extmdef
    return extobj
