var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";
document.head.appendChild(script);
script.onload = function () {
tinymce.init({
            selector: "#id_body",
            content_style: "div {margin: 10px; border: 5px solid red; padding: 3px}",
            plugins: ["advlist autolink lists charmap preview hr anchor",
               "pagebreak code nonbreaking table contextmenu directionality paste link fullscreen image imagetools media insertdatetime searchreplace textcolor wordcount textpattern codesample"],
            toolbar1: "styleselect | bold italic underline | pagebreak code preview | undo redo | link | image media | insertdatetime | searchreplace",
            toolbar2: "alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | forecolor backcolor | codesample | fullscreen",
            relative_urls: false,
            remove_script_host: false,
            convert_urls: true,
        });
}