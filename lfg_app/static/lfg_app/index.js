document.addEventListener('DOMContentLoaded', () => {
    const API_URL = window.location.href;
    const proposalForm = document.getElementById('proposal-form');
    const messageContainer = document.getElementById('message-container');
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
        const data = {};
        for (let [key, value] of formData.entries()) {
            data[key] = value;
        }
        var csrf_token = getCookie('csrftoken')
        fetch(API_URL + 'proposals/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrf_token},
            body: JSON.stringify(data)
        }).then(response => response.json())
        .then(data => {
            console.log(data)
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