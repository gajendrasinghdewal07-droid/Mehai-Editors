async function upload() {
    let file = document.getElementById("video").files[0];
    let prompt = document.getElementById("prompt").value;

    let formData = new FormData();
    formData.append("file", file);
    formData.append("prompt", prompt);

    let res = await fetch("/edit", {
        method: "POST",
        body: formData
    });

    let data = await res.json();
    alert("Video Ready: " + data.video);
}
