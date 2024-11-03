document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('addChatBtn').onclick = function() {
        document.getElementById('modal').classList.remove('hidden');
    }

    document.querySelector('.close').onclick = function() {
        document.getElementById('modal').classList.add('hidden');
    }

    document.getElementById('chatType').onchange = function() {
        const selectedType = this.value;
        document.getElementById('groupOptions').classList.toggle('hidden', selectedType !== 'group');
        document.getElementById('privateOptions').classList.toggle('hidden', selectedType !== 'private');
    }

    document.getElementById('createChatBtn').onclick = function() {
        const chatType = document.getElementById('chatType').value;

        if (chatType === 'group') {
            const groupName = document.getElementById('groupName').value;
            const participants = Array.from(document.getElementById('participants').selectedOptions).map(option => option.value);
            alert(Группа "${groupName}" создана с участниками: ${participants.join(', ')});
        } else {
            const phoneNumber = document.getElementById('phoneNumber').value;
            alert(Чат создан с номером телефона: ${phoneNumber});
        }

        document.getElementById('modal').classList.add('hidden');
    }
});
