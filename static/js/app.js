document.addEventListener('DOMContentLoaded', () => {
    // Register service worker
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/static/service-worker.js')
            .then(registration => {
                console.log('ServiceWorker registration successful');
            })
            .catch(err => {
                console.log('ServiceWorker registration failed: ', err);
            });
    }

    // Initialize PWA features
    if ('Notification' in window) {
        Notification.requestPermission();
    }

    // Add event listeners
    document.querySelectorAll('form').forEach(form => {
        // Skip authentication forms (login and register) for special handling
        if (!form.closest('.login-container') && !form.closest('.register-container')) {
            form.addEventListener('submit', handleFormSubmit);
        }
    });
});

async function handleFormSubmit(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);
    const url = form.getAttribute('action');
    const method = form.getAttribute('method') || 'GET';

    try {
        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(Object.fromEntries(formData)),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        handleResponse(data, form);
    } catch (error) {
        console.error('Error:', error);
        showNotification('Error', error.message, 'error');
    }
}

function handleResponse(data, form) {
    if (data.success) {
        showNotification('Success', data.message, 'success');
        form.reset();
        // Update UI based on response
        updateUI(data);
    } else {
        showNotification('Error', data.message, 'error');
    }
}

function showNotification(title, message, type = 'info') {
    if ('Notification' in window && Notification.permission === 'granted') {
        new Notification(title, {
            body: message,
            icon: '/static/icons/icon-192x192.png',
        });
    }
}

function updateUI(data) {
    // Update transaction list
    if (data.transactions) {
        updateTransactionList(data.transactions);
    }
    // Update balance
    if (data.balance) {
        updateBalance(data.balance);
    }
}

function updateTransactionList(transactions) {
    const transactionList = document.querySelector('.recent-transactions table tbody');
    if (!transactionList) return;

    transactionList.innerHTML = transactions.map(transaction => `
        <tr>
            <td>${new Date(transaction.date).toLocaleDateString()}</td>
            <td>${transaction.description}</td>
            <td>${transaction.category}</td>
            <td>$${transaction.amount.toFixed(2)}</td>
        </tr>
    `).join('');
}

function updateBalance(balance) {
    const balanceElement = document.querySelector('.stat-value');
    if (balanceElement) {
        balanceElement.textContent = `$${balance.toFixed(2)}`;
    }
}
