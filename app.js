async function upload() {

    let file = document.getElementById("video").files[0];
    let prompt = document.getElementById("prompt").value;

    if (!file) {
        alert("Select a video first");
        return;
    }

    let formData = new FormData();

    formData.append("file", file);
    formData.append("prompt", prompt);

    let response = await fetch("/edit", {
        method: "POST",
        body: formData
    });

    let data = await response.json();

    document.getElementById("result").innerText =
        "Uploaded: " + data.filename +
        " | Prompt: " + data.prompt;
}
