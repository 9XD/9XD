/**
 * Created by jelly on 1/14/17.
 */
const editorView = new Vue({
    el: '#editor',
    data: {
        input: '# Markdown editor',
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
        },
    },
    methods: {
        update: _.debounce(function (e) {
            this.input = e.target.value
        }, 300)
    }
});
