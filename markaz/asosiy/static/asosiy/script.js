// Navbar linklariga bosing va animatsiya
document.querySelectorAll('.navbar .links a').forEach(link => {
    link.addEventListener('click', () => {
        alert(`Siz "${link.textContent}" sahifasini ochmoqchisiz!`);
    });
});

// Tugma bosilganda foydalanuvchiga xabar chiqarish
document.querySelectorAll('button').forEach(button => {
    button.addEventListener('click', () => {
        alert('Bu tugma faoliyatga tayyor!');
    });
});
