from flask import Flask, abort, render_template, request
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent
DB = BASE / "psicologos.db"

app = Flask(__name__)

PSICOLOGOS_DEMOSTRACAO = [
    ("Dra. Ana Martins", "CRP 00/00000", "Psicologia clínica", "Ansiedade, autoestima e transições de vida.", "Lisboa", "Online e presencial", "Português, espanhol", "Abordagem cognitivo-comportamental com escuta acolhedora."),
    ("Dr. Bruno Costa", "CRP 00/00001", "Terapia de casal", "Comunicação, conflitos e vínculos afetivos.", "Porto", "Online", "Português", "Atendimento focado em diálogos mais seguros e objetivos compartilhados."),
    ("Dra. Carla Nunes", "CRP 00/00002", "Psicologia infantil", "Emoções, adaptação escolar e orientação a famílias.", "Coimbra", "Presencial", "Português", "Trabalho lúdico em parceria com responsáveis e escola quando necessário."),
    ("Dr. Diego Ramos", "CRP 00/00003", "LGBTQIA+", "Identidade, relações e saúde emocional.", "Braga", "Online e presencial", "Português, inglês", "Espaço afirmativo, confidencial e livre de julgamentos."),
    ("Dra. Elena Ruiz", "CRP 00/00004", "Burnout e carreira", "Estresse, limites e mudanças profissionais.", "Faro", "Online", "Português, espanhol", "Acompanhamento para recuperar clareza, energia e equilíbrio."),
    ("Dr. Felipe Moura", "CRP 00/00005", "Luto", "Perdas, despedidas e reorganização emocional.", "Setúbal", "Online e presencial", "Português", "Ritmo respeitoso para acolher experiências difíceis e singulares."),
]


def conectar():
    conexao = sqlite3.connect(DB)
    conexao.row_factory = sqlite3.Row
    return conexao


def preparar_base():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS psicologos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                registro TEXT NOT NULL,
                especialidade TEXT NOT NULL,
                temas TEXT NOT NULL,
                cidade TEXT NOT NULL,
                modalidade TEXT NOT NULL,
                idiomas TEXT NOT NULL,
                apresentacao TEXT NOT NULL,
                email_publico TEXT,
                telefone_publico TEXT,
                site_publico TEXT,
                endereco_publico TEXT,
                codigo_postal TEXT,
                pais TEXT,
                valor_sessao TEXT,
                disponibilidade TEXT,
                foto_url TEXT,
                fonte_url TEXT,
                origem TEXT NOT NULL DEFAULT 'demonstração',
                estado_verificacao TEXT NOT NULL DEFAULT 'pendente',
                extraido_em TEXT,
                atualizado_em TEXT,
                dados_ia_json TEXT,
                conteudo_origem TEXT
            )
        """)
        campos = {
            "email_publico": "TEXT", "telefone_publico": "TEXT", "site_publico": "TEXT",
            "endereco_publico": "TEXT", "codigo_postal": "TEXT", "pais": "TEXT",
            "valor_sessao": "TEXT", "disponibilidade": "TEXT", "foto_url": "TEXT",
            "fonte_url": "TEXT", "origem": "TEXT NOT NULL DEFAULT 'demonstração'",
            "estado_verificacao": "TEXT NOT NULL DEFAULT 'pendente'", "extraido_em": "TEXT",
            "atualizado_em": "TEXT", "dados_ia_json": "TEXT", "conteudo_origem": "TEXT"
        }
        existentes = {linha[1] for linha in conexao.execute("PRAGMA table_info(psicologos)")}
        for campo, definicao in campos.items():
            if campo not in existentes:
                conexao.execute(f"ALTER TABLE psicologos ADD COLUMN {campo} {definicao}")
        conexao.execute("CREATE UNIQUE INDEX IF NOT EXISTS indice_url_fonte ON psicologos(fonte_url) WHERE fonte_url IS NOT NULL")
        quantidade = conexao.execute("SELECT COUNT(*) FROM psicologos").fetchone()[0]
        if quantidade == 0:
            conexao.executemany("""
                INSERT INTO psicologos
                (nome, registro, especialidade, temas, cidade, modalidade, idiomas, apresentacao)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, PSICOLOGOS_DEMOSTRACAO)


def opcoes(campo):
    with conectar() as conexao:
        return [linha[0] for linha in conexao.execute(
            f"SELECT DISTINCT {campo} FROM psicologos ORDER BY {campo} COLLATE NOCASE"
        )]


@app.route("/")
def inicio():
    return render_template(
        "inicio.html",
        especialidades=opcoes("especialidade"),
        cidades=opcoes("cidade")
    )


@app.route("/buscar")
def buscar():
    texto = request.args.get("q", "").strip()
    especialidade = request.args.get("especialidade", "").strip()
    cidade = request.args.get("cidade", "").strip()
    modalidade = request.args.get("modalidade", "").strip()

    condicoes = []
    parametros = []

    if texto:
        palavras = texto.split()[:8]
        for palavra in palavras:
            condicoes.append("""(
                LOWER(nome) LIKE ? OR LOWER(especialidade) LIKE ? OR
                LOWER(temas) LIKE ? OR LOWER(apresentacao) LIKE ? OR LOWER(idiomas) LIKE ?
            )""")
            parametros.extend([f"%{palavra.lower()}%"] * 5)
    if especialidade:
        condicoes.append("especialidade = ?")
        parametros.append(especialidade)
    if cidade:
        condicoes.append("cidade = ?")
        parametros.append(cidade)
    if modalidade:
        condicoes.append("modalidade = ?")
        parametros.append(modalidade)

    sql = "SELECT * FROM psicologos"
    if condicoes:
        sql += " WHERE " + " AND ".join(condicoes)
    sql += " ORDER BY nome COLLATE NOCASE"

    with conectar() as conexao:
        resultados = [dict(linha) for linha in conexao.execute(sql, parametros)]

    return render_template(
        "resultados.html",
        resultados=resultados,
        q=texto,
        especialidade=especialidade,
        cidade=cidade,
        modalidade=modalidade,
        especialidades=opcoes("especialidade"),
        cidades=opcoes("cidade")
    )


@app.route("/psicologo/<int:identificador>")
def perfil(identificador):
    with conectar() as conexao:
        psicologo = conexao.execute(
            "SELECT * FROM psicologos WHERE id = ?", (identificador,)
        ).fetchone()
    if psicologo is None:
        abort(404)
    return render_template("perfil.html", psicologo=dict(psicologo))


preparar_base()

if __name__ == "__main__":
    app.run(debug=True)
