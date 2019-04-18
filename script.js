var chat = document.getElementById("chat");
var kirim = document.getElementById("kirim");
var message = document.getElementById("message");
var form = document.getElementById("formchat");
var next = document.getElementById("next");
var awal = document.getElementById("awal");
var konten = document.getElementById("konten");

function sleep(milliseconds) {
    var start = new Date().getTime();
    for (var i = 0; i < 1e7; i++) {
      if ((new Date().getTime() - start) > milliseconds){
        break;
      }
    }
  }

next.addEventListener("click", function(){
    konten.removeAttribute("hidden");
    awal.setAttribute("hidden", "true");
})

function getanswer(mes){
    var pil;
    if (document.getElementById("one").checked == true){
        pil = 1;
    } else{
        pil = 2;
    }

    var node = document.createElement("div");
    node.classList.add("bot");
    node.classList.add("animated");
    node.classList.add("bounce");
    var m = document.createElement("p");
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function(){
        if (xhr.readyState == 4 && xhr.status == 200){
            m.innerHTML = xhr.responseText;
            node.appendChild(m);
            chat.appendChild(node);
            chat.scrollTop = chat.scrollHeight+1200;
		}
    }
    xhr.open('GET', 'BE/answer.php?message=' + mes + '&pil=' + pil);
    xhr.send();
}

kirim.addEventListener("click", function(e){
    e.preventDefault();
    var node = document.createElement("div");
    node.classList.add("player");
    node.classList.add("animated");
    node.classList.add("bounce");
    var m = document.createElement("p");
    var pesan = message.value;
    var text = document.createTextNode(pesan);
    m.appendChild(text);
    node.appendChild(m);
    chat.appendChild(node);
    getanswer(pesan);
    form.reset();
})

