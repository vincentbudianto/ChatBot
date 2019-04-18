<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <link href="style.css" rel="stylesheet">
        <link href="animation.css" rel="stylesheet">
        <link href="https://fonts.googleapis.com/css?family=Noto+Sans+JP" rel="stylesheet">
        <title>Simple Chat Bot</title>
    </head>

    <body>
        <div class="container" id="awal">
            <div class="card animated fadeIn delay-1s">
                <h2>Pilih Metode Exact Matching</h2>  
                <ul>
                    <li>
                        <input type="radio" name="name" id="one" checked />
                        <label for="one">Boyer Moore</label>
                        <div class="check"></div>
                    </li>
                    <li>
                        <input type="radio" name="name" id="two" />
                        <label for="two">KMP</label>
                        <div class="check"></div>
                    </li>
                </ul>
                <button type="button" id="next">NEXT</button>
            </div>
        </div>
        <div id="konten" hidden>
            <!-- <h1>Tukang PHP Simple Chat Bot</h1> -->
            <div class="container">
                <div class="avatar animated fadeIn">
                    <img src="avatar-1.png" alt="">
                </div>
                <div class="roomchat animated fadeIn">
                    <div id="header">
                        <img src="avatar-1.png">
                        <div class="status">
                            <h4>Bot Name</h4>
                            <p>online</p>
                        </div>
                    </div>
                    <div class="chat" id="chat">
                        <div class="bot animated bounce">
                            <p>Halo, ada yang bisa saya bantu?</p>
                        </div>
                    </div>
                    <div class="input">
                        <form method="POST" id="formchat">
                            <input type="text" id="message" placeholder="Masukkan pesan ..." autofocus autocomplete="off">
                            <input class="submit" id="kirim" type="submit" value="Kirim">
                        </form>
                    </div>
                </div>
            </div>
        </div>
        <script src="script.js"></script>
    </body>
</html>