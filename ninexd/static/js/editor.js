/**
 * Created by jelly on 1/14/17.
 */
const content_div_el = document.getElementById("div_id_content");
const content_textarea_el = document.getElementById("id_content");

content_div_el.innerHTML = "<label for=\"id_content\" class=\"form-control-label requiredField\">\r\n        Content<span class=\"asteriskField\">*<\/span>\r\n    <\/label>\r\n    <div id=\"editor\" class=\"\">\r\n        "  + content_textarea_el.outerHTML + "\r\n        <div v-html=\"compiledMarkdown\"><\/div>\r\n        <div v-html=\"compiler\" v-show=\"false\"><\/div>\r\n    <\/div>";
const content_value = function () {
    const exist_value = content_textarea_el.innerText;
    if (exist_value == "") {
        return "# Markdown editor"
    } else {
        return exist_value;
    }
};

new Vue({
    el: '#editor',
    data: {
        input: content_value(),
        compiledMarkdown: ''
    },
    computed: {
        compiler: function () {
            const cm = this;
            const form_data = new FormData();
            form_data.append('text', this.input);
            const options = {
                headers: {
                    "X-CSRFToken": document.getElementsByName('csrfmiddlewaretoken')[0].value,
                },
                body: {
                    text: this.input
                }
            };

            cm.$http.post('/common/convert-markdown', form_data, options).then(
                function (response) {
                    this.compiledMarkdown = response.data;
                }, function (response) {
                    response.data;
                });
        }
    },
    methods: {
        update: _.debounce(function (e) {
            this.input = e.target.value
        }, 300)
    }
});
