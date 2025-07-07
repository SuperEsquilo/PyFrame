# PyFrame
Um site para conhecer meus serviços de criação de interfaces com python

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <title>PyFrame - Interface para Sistemas de Cadastro em Python</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- Google Fonts: Comfortaa & Roboto -->
    <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@700&family=Roboto:wght@400;700&display=swap"
        rel="stylesheet">
    <style>
        :root {
            --primary: #4F46E5;
            --primary-dark: #312E81;
            --accent: #F59E42;
            --bg: #18181B;
            --surface: #232336;
            --text: #fff;
            --text-muted: #A1A1AA;
            --card-radius: 18px;
            --shadow: 0 4px 24px rgba(0, 0, 0, 0.18);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Roboto', Arial, sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
        }

        header {
            background: var(--primary);
            box-shadow: var(--shadow);
            padding: 0;
            position: relative;
            height: 90px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .logo {
            font-family: 'Comfortaa', cursive;
            font-size: 2.2rem;
            color: #fff;
            letter-spacing: 2px;
            margin-left: 40px;
            user-select: none;
        }

        .menu-btn {
            position: absolute;
            top: 50%;
            right: 40px;
            transform: translateY(-50%);
            background: var(--accent);
            color: var(--primary-dark);
            font-family: 'Comfortaa', cursive;
            font-size: 1.1rem;
            padding: 12px 32px;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            font-weight: bold;
            box-shadow: var(--shadow);
            transition: background 0.2s, color 0.2s;
        }

        .menu-btn:hover {
            background: #fff;
            color: var(--primary-dark);
        }

        .hero {
            background: linear-gradient(120deg, var(--primary-dark) 60%, var(--primary) 100%);
            padding: 70px 0 50px 0;
            text-align: center;
        }

        .hero h2 {
            font-family: 'Comfortaa', cursive;
            font-size: 2.3rem;
            color: var(--accent);
            margin-bottom: 18px;
        }

        .hero p {
            font-size: 1.2rem;
            color: #fff;
            margin-bottom: 22px;
        }

        .cta-btn {
            background: var(--accent);
            color: var(--primary-dark);
            font-family: 'Comfortaa', cursive;
            font-size: 1.1rem;
            padding: 14px 38px;
            border: none;
            border-radius: 30px;
            cursor: pointer;
            font-weight: bold;
            box-shadow: var(--shadow);
            transition: background 0.2s, color 0.2s;
        }

        .cta-btn:hover {
            background: #fff;
            color: var(--primary-dark);
        }

        .section {
            max-width: 1100px;
            margin: 48px auto;
            padding: 0 24px;
        }

        .section-title {
            font-family: 'Comfortaa', cursive;
            font-size: 2rem;
            color: var(--accent);
            margin-bottom: 28px;
            text-align: center;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 32px;
        }

        .card {
            background: var(--surface);
            border-radius: var(--card-radius);
            box-shadow: var(--shadow);
            padding: 28px 20px 22px 20px;
            text-align: center;
            transition: transform 0.18s;
            position: relative;
            cursor: pointer;
        }

        .card:hover {
            transform: translateY(-8px) scale(1.03);
        }

        .card-icon {
            font-size: 2.5rem;
            margin-bottom: 14px;
            color: var(--accent);
        }

        .card h3 {
            font-family: 'Comfortaa', cursive;
            font-size: 1.3rem;
            color: var(--accent);
            margin-bottom: 10px;
        }

        .card p {
            font-size: 1rem;
            color: #eee;
            margin-bottom: 10px;
        }

        .about {
            display: flex;
            flex-wrap: wrap;
            gap: 36px;
            align-items: center;
            justify-content: center;
        }

        .about-text {
            flex: 1 1 320px;
            min-width: 280px;
        }

        .about-img {
            flex: 1 1 320px;
            min-width: 220px;
            text-align: center;
        }

        .about-img img {
            width: 260px;
            border-radius: 30px;
            box-shadow: var(--shadow);
        }

        .showcase {
            margin: 48px auto 0 auto;
            max-width: 1100px;
            padding: 0 24px;
        }

        .showcase-title {
            font-family: 'Comfortaa', cursive;
            font-size: 1.5rem;
            color: var(--accent);
            margin-bottom: 18px;
            text-align: center;
        }

        .showcase-imgs {
            display: flex;
            gap: 24px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .showcase-imgs img {
            width: 320px;
            border-radius: 18px;
            box-shadow: var(--shadow);
            background: #fff;
            object-fit: cover;
        }

        footer {
            background: var(--surface);
            color: #aaa;
            text-align: center;
            padding: 24px 0 10px 0;
            font-size: 1rem;
            margin-top: 40px;
        }

        /* Responsive */
        @media (max-width: 700px) {
            .about {
                flex-direction: column;
            }

            .about-img img {
                width: 90vw;
                max-width: 320px;
            }

            .section {
                padding: 0 8px;
            }

            header {
                flex-direction: column;
                height: auto;
            }

            .logo {
                margin: 20px 0 0 0;
            }

            .menu-btn {
                position: static;
                margin: 20px 0 0 0;
                transform: none;
            }

            .showcase-imgs img {
                width: 98vw;
                max-width: 340px;
            }
        }
    </style>
</head>

<body>
    <header>
        <div class="logo">PyFrame</div>
        <a href="https://wa.me/5518991471530"><button class="menu-btn">Entrar em contato</button></a>
    </header>
    <section class="hero">
        <h2>Encomende a criação interfaces gráficas profissionais em Python para sistemas de cadastro</h2>
        <p>
            O <b>PyFrame</b> é a solução moderna para quem deseja criar sistemas de cadastro com interfaces intuitivas,
            responsivas e visualmente incríveis usando Python.<br>
            Ideal para empresas, desenvolvedores e projetos acadêmicos.
        </p>
        <button class="cta-btn" onclick="scrollToFeatures()">Ver Recursos</button>
    </section>
    <section class="section" id="features">
        <div class="section-title">Recursos do PyFrame</div>
        <div class="features-grid">
            <div class="card">
                <div class="card-icon">🖥️</div>
                <h3>Design Moderno</h3>
                <p>Componentes visuais inspirados em Material Design e CustomTkinter, com temas escuros e claros.</p>
            </div>
            <div class="card">
                <div class="card-icon">⚡</div>
                <h3>Fácil Integração</h3>
                <p>Integre rapidamente com bancos de dados SQLite, MySQL ou arquivos JSON para persistência de dados.
                </p>
            </div>
            <div class="card">
                <div class="card-icon">🔒</div>
                <h3>Segurança</h3>
                <p>Recursos de autenticação, permissões e criptografia para proteger seus dados de cadastro.</p>
            </div>
            <div class="card">
                <div class="card-icon">📝</div>
                <h3>Formulários Personalizáveis</h3>
                <p>Monte telas de cadastro, edição e consulta com campos dinâmicos e validação automática.</p>
            </div>
            <div class="card">
                <div class="card-icon">📦</div>
                <h3>Exportação de Dados</h3>
                <p>Exporte registros para Excel, PDF ou CSV com apenas um clique.</p>
            </div>
            <div class="card">
                <div class="card-icon">🌐</div>
                <h3>Documentação Completa</h3>
                <p>Guia detalhado, exemplos práticos e suporte para desenvolvedores de todos os níveis.</p>
            </div>
        </div>
    </section>
    <section class="section" id="sobre">
        <div class="section-title">Sobre o PyFrame</div>
        <div class="about">
            <div class="about-text">
                <p>
                    O PyFrame nasceu para facilitar a vida de quem precisa criar sistemas de cadastro robustos e bonitos
                    em Python, sem complicação.
                    Com um sistema intuitivo e componentes visuais modernos, você foca no que importa: a lógica do seu
                    sistema.
                </p>
                <p>
                    Seja para controle de clientes, produtos, funcionários ou qualquer outro tipo de registro, o PyFrame
                    entrega produtividade e resultado profissional.
                </p>
            </div>
            <div class="about-img">
                <img src="https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=600&q=80"
                    alt="Equipe PyFrame">
            </div>
        </div>
    </section>
    <footer>
        © 2025 PyFrame. Todos os direitos reservados.
    </footer>
    <script>
        function scrollToFeatures() {
            document.getElementById('features').scrollIntoView({ behavior: 'smooth' });
        }
    </script>
</body>

</html>
