r"""
numberrex -> regex

reales

\Nint -> \d+
\Ndec -> \d+\.\d+
\Nreal -> \d+(?:\.\d+)?

cplx-imag

\Nimag -> \d+(?:\.\d+)?i
\Npcplx -> \d+(?:\.\d+)?\s*\+\s*\d+(?:\.\d+)?i
\Nncplx -> \d+(?:\.\d+)?\s*-\s*\d+(?:\.\d+)?i
\Ncplx -> \d+(?:\.\d+)?\s*[+-]\s*\d+(?:\.\d+)?i

signos

\Ss -> [+-]
\Sns -> [+-]?

signos-complejo-imag-real

\Ssi -> [+-]\d+(?:\.\d+)?i
\Ssc -> [+-]\d+(?:\.\d+)?\s*[+-]\s*\d+(?:\.\d+)?i
\Ssr -> [+-]\d+(?:\.\d+)?

\Si -> [+-]?\d+(?:\.\d+)?i
\Sc -> [+-]?\d+(?:\.\d+)?\s*[+-]\s*\d+(?:\.\d+)?i
\Sr -> [+-]?\d+(?:\.\d+)?

otro

\Nc = [+-]?(?:\d+(?:\.\d*)?|\.\d+)[eE][+-]?\d+
"""
import re

class nre:
    flags = {"D": re.DOTALL, "M": re.MULTILINE, "V": re.VERBOSE, "I": re.IGNORECASE, "U": re.UNICODE}

    @classmethod
    def get_flags(cls, chars: str):
        total = 0
        for ch in chars:
            total |= cls.flags.get(ch.upper(), 0)
        return total
    patts = {
        # reales
        r"\Nint":  r"\d+",
        r"\Ndec":  r"\d+\.\d+",
        r"\Nreal": r"\d+(?:\.\d+)?",

        # complejos / imaginarios
        r"\Nimag":  r"\d+(?:\.\d+)?i",
        r"\Npcplx": r"\d+(?:\.\d+)?\s*\+\s*\d+(?:\.\d+)?i",
        r"\Nncplx": r"\d+(?:\.\d+)?\s*-\s*\d+(?:\.\d+)?i",
        r"\Ncplx":  r"\d+(?:\.\d+)?\s*[+-]\s*\d+(?:\.\d+)?i",

        # signos
        r"\Ss":   r"[+-]",
        r"\Sns":  r"[+-]?",

        # signos + conjuntos reales/imag/complejos
        r"\Ssi": r"[+-]\d+(?:\.\d+)?i",
        r"\Ssc": r"[+-]\d+(?:\.\d+)?\s*[+-]\s*\d+(?:\.\d+)?i",
        r"\Ssr": r"[+-]\d+(?:\.\d+)?",

        r"\Si":  r"[+-]?\d+(?:\.\d+)?i",
        r"\Sc":  r"[+-]?\d+(?:\.\d+)?\s*[+-]\s*\d+(?:\.\d+)?i",
        r"\Sr":  r"[+-]?\d+(?:\.\d+)?",
        
        #otro
        r"\Nc":  r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)[eE][+-]?\d+"
    }
    @staticmethod
    def ToRe(patt: str, flags=0) -> str:
        """Convierte un patrón Numberrex en un regex normal."""
        keys = sorted(nre.patts.keys(), key=len, reverse=True)
        for k in keys:
            patt = re.sub(re.escape(k), nre.patts[k], patt)
        return re.compile(patt, flags=flags)
    @staticmethod
    def sub(patt, repl, string, flags=0):
        p = nre.ToRe(patt, flags=flags)
        return p.sub(repl, string)
    @staticmethod
    def match(patt, string, flags=0):
        p = nre.ToRe(patt, flags=flags)
        return p.match(string)
    @staticmethod
    def finditer(patt, string, flags=0):
        p = nre.ToRe(patt, flags=flags)
        return p.finditer(string)
    @staticmethod
    def findall(patt, string, flags=0):
        p = nre.ToRe(patt, flags=flags)
        return p.findall(string)
    @staticmethod
    def fullmatch(patt, string, flags=0):
        p = nre.ToRe(patt, flags=flags)
        return p.fullmatch(string)