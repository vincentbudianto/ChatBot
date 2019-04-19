var chat = document.getElementById("chat");
var kirim = document.getElementById("kirim");
var message = document.getElementById("message");
var form = document.getElementById("formchat");
var next1 = document.getElementById("next1");
var next2 = document.getElementById("next2");
var awal = document.getElementById("awal");
var konten = document.getElementById("konten");
var persentase = document.getElementById("persentase");
var range = document.getElementById("input")

next1.addEventListener("click", function(){
    persentase.removeAttribute("hidden");
    awal.setAttribute("hidden", "true");
})

next2.addEventListener("click", function(){
  konten.removeAttribute("hidden");
  persentase.setAttribute("hidden", "true");
})

range.addEventListener("change", function(){
  nilai.innerHTML = '<p>Persentase Kemiripan : <span style="font-weight: bold">'+ range.value +'%</span></p>';
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
    xhr.open('GET', 'BE/answer.php?message=' + mes + '&pil=' + pil + '&range=' + range.value);
    xhr.send();
}

function animate(){
    document.getElementById("avatar").innerHTML = '<img src="avatar-2.png" alt="">'
}

kirim.addEventListener("click", function(e){
    e.preventDefault();
    document.getElementById("avatar").innerHTML = '<img src="avatar-1.png" alt="">'
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
    setTimeout(animate, 2000)
})

