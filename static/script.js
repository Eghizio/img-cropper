const sendImage = async (img) => {
    const response = await fetch("/images", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ img, hello: "there" })
    });

    const data = await response.json();
    
    if(data.img){
        renderImage(data.img, "img#img-response");
    }
};

const renderImage = (b64, selector) => {
    const img = document.querySelector(selector);
    img.src = b64;
};

const handlePaste = (event) => {
    const items = (event.clipboardData || event.originalEvent.clipboardData).items;
    // console.log(JSON.stringify(items)); // might give you mime types

    for (const item of items) {
        if (item.kind === "file") {
            const reader = new FileReader();

            reader.addEventListener("load", (event) => {
                const base64 = event.target.result;
                // console.log(base64); // data url!
                sendImage(base64);
                renderImage(base64, "img#img");
            });

            const blob = item.getAsFile();
            reader.readAsDataURL(blob);
        }
    }
};

document.addEventListener("paste", handlePaste);
