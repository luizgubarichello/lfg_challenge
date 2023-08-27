document.addEventListener('DOMContentLoaded', () => {
    const API_URL = window.location.href;
    const proposalForm = document.getElementById('proposal-form');
    const messageContainer = document.getElementById('message-container');
    
    global_fieldData = []
    fetch(API_URL + 'fields/') 
    .then(response => response.json())
    .then(data => { 
        for (let fieldData of data) { 
            global_fieldData.push(fieldData)
            const field = createProposalField(fieldData);
            proposalForm.appendChild(field);
        }
        if (global_fieldData.length === 0) {
            const nothing = createElement('div', {class: 'field'}, 'Periodo de propostas fechado!');
            proposalForm.appendChild(nothing);
        } else {
            const button = createElement('button', {type: 'submit'}, 'Enviar Proposta');
            proposalForm.appendChild(button);
            proposalForm.addEventListener('submit', submitProposal);
        }
    }).catch(error => {
        console.error(error);
        const message = createMessage('error', 'Ocorreu um erro ao carregar os campos de proposta. Por favor, recarregue a página.');
        messageContainer.innerHTML = '';
        messageContainer.appendChild(message);
    });

    proposalForm.addEventListener('submit', submitProposal);

    function createElement(tag, attributes, content) {
        const element = document.createElement(tag);
        for (let key in attributes) {
            element.setAttribute(key, attributes[key]);
        }
        if (content) {
            element.textContent = content;
        }
        return element;
    }

    function createInputField(type, fieldData) {
        let input;
        switch (type) {
            case 'text':
                input = createElement('input', {type: 'text', name: fieldData.name, required: fieldData.required});
                break; 
            case 'number':
                input = createElement('input', {type: 'number', name: fieldData.name, required: fieldData.required});
                break; 
            case 'date':
                input = createElement('input', {type: 'date', name: fieldData.name, required: fieldData.required});
                break; 
            default:
                input = null;
                break; 
        }
        return input;
    }

    function createProposalField(fieldData) {
        const field = createElement('div', {class: 'field'});
        const label = createElement('label', {for: fieldData.name}, fieldData.label);
        const input = createInputField(fieldData.type, fieldData);
        if (input) {
            field.appendChild(label);
            field.appendChild(input);
        }
        return field;
    }

    function createMessage(type, content) {
        const message = createElement('div', {class: `message ${type}`}, content);
        return message;
    }

    function getCookie(cname) {
        let name = cname + "=";
        let decodedCookie = decodeURIComponent(document.cookie);
        let ca = decodedCookie.split(';');
        for(let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }

    function submitProposal(event) {
        event.preventDefault();
        const formData = new FormData(proposalForm);
        const fields = [];
        let i = 0;
        for (let [key, value] of formData.entries()) {
            if(i != 0){
                field = {};
                field_id = -1;
                for (i in global_fieldData) {
                    console.log(global_fieldData[i])
                    if (global_fieldData[i]['name'] === key){
                        field_id = global_fieldData[i]['id'];
                    }
                }
                field["field"] = field_id;
                field["value"] = value;
                fields.push(field);
            }
            i++;
        }
        data = {fields};
        var csrf_token = getCookie('csrftoken');
        fetch(API_URL + 'proposals/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrf_token},
            body: JSON.stringify(data)
        }).then(response => response.json())
        .then(data => {
            if (data.id) {
                const message = createMessage('success', `Proposta enviada com sucesso. O número da sua proposta é ${data.id}.`);
                messageContainer.innerHTML = '';
                messageContainer.appendChild(message);
                proposalForm.reset();
            } else {
                const message = createMessage('error', `Ocorreu um erro ao enviar a proposta. Por favor, tente novamente.`);
                messageContainer.innerHTML = '';
                messageContainer.appendChild(message);
            }
        }).catch(error => {
            console.error(error);
            const message = createMessage('error', `Ocorreu um erro ao enviar a proposta. Por favor, tente novamente.`);
            messageContainer.innerHTML = '';
            messageContainer.appendChild(message);
        });
    }

})