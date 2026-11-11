"""Cálculos da sessão de antropometria (perfil sintético de demonstração).

Uso: python calcula_antropometria.py            -> roda o self-check
     python calcula_antropometria.py sessao.json -> calcula uma sessão nova
sessao.json: {"idade":36,"altura_cm":175,"peso_kg":76.5,"pescoco":37.5,"abdomen":84.0,"cintura_min":81.0,
              "quadril":95.0,"braco_relaxado":{"D":33.0,"E":32.5},"triceps_mm":{"D":9.0,"E":8.0},
              "dobras_mm":{"peitoral":12.0,"axilar":8.0,"triceps":9.0,"subescapular":11.0,"abdominal":14.0,"supra":12.0,"coxa":10.0}}
Dobras = mediana de 3 pinçamentos já calculada por quem mede. Σ7 exige as 7; sem elas, só Σ4 autoaplicável.
"""
import json, math, sys

S4 = ("peitoral", "abdominal", "supra", "coxa")  # autoaplicáveis


def calcula(d):
    h, peso, idade = d["altura_cm"], d["peso_kg"], d["idade"]
    out = {}
    f = d["dobras_mm"]
    out["sigma4"] = sum(f[k] for k in S4)
    if len(f) >= 7:
        s7 = sum(f.values())
        dens = 1.112 - 0.00043499 * s7 + 0.00000055 * s7**2 - 0.00028826 * idade  # Jackson-Pollock 7, homem
        out["sigma7"] = s7
        out["jp7_pct"] = round(495 / dens - 450, 1)  # Siri
    # US Navy, métrico, usa abdômen (média de 3 níveis)
    dens_n = 1.0324 - 0.19077 * math.log10(d["abdomen"] - d["pescoco"]) + 0.15456 * math.log10(h)
    out["navy_pct"] = round(495 / dens_n - 450, 1)
    out["rcq_abdomen"] = round(d["abdomen"] / d["quadril"], 3)
    out["rcq_minima"] = round(d["cintura_min"] / d["quadril"], 3)
    out["cintura_estatura"] = round(d["abdomen"] / h, 3)
    for lado in ("D", "E"):
        cmb = d["braco_relaxado"][lado] - math.pi * d["triceps_mm"][lado] / 10
        out[f"cmb_{lado}"] = round(cmb, 2)
        out[f"ama_{lado}"] = round(cmb**2 / (4 * math.pi) - 10, 1)  # AMA corrigida, homem
    return out


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(json.dumps(calcula(json.load(open(sys.argv[1]))), indent=1, ensure_ascii=False))
    else:
        s1 = dict(idade=36, altura_cm=175, peso_kg=76.5, pescoco=37.5, abdomen=84.0, cintura_min=81.0, quadril=95.0,
                  braco_relaxado={"D": 33.0, "E": 32.5}, triceps_mm={"D": 9.0, "E": 8.0},
                  dobras_mm=dict(peitoral=12.0, axilar=8.0, triceps=9.0, subescapular=11.0, abdominal=14.0, supra=12.0, coxa=10.0))
        r = calcula(s1)
        # Perfil sintético: Σ7 76, Σ4 48, JP7 11.9, Navy 16.5, RCQ 0.884, Cint/Est 0.480, CMB 30.17/29.99, AMA 62.4/61.6
        assert (r["sigma7"], r["sigma4"], r["jp7_pct"]) == (76.0, 48.0, 11.9), r
        assert abs(r["navy_pct"] - 16.5) <= 0.3, r
        assert (r["rcq_abdomen"], r["cintura_estatura"]) == (0.884, 0.48), r
        assert (r["cmb_D"], r["cmb_E"], r["ama_D"], r["ama_E"]) == (30.17, 29.99, 62.4, 61.6), r
        print("self-check OK", r)
