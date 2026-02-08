const box = document.getElementById('scatterBox');
const colors = ['red', 'blue', 'yellow'];
const totalBalls = 100;

const boxSize = 500;
const ballSize = 8;

for (let i = 0; i < totalBalls; i++) {
    const ball = document.createElement('div');
    const color = colors[Math.floor(Math.random() * colors.length)];

    const x = Math.random() * (boxSize - ballSize);
    const y = Math.random() * (boxSize - ballSize);

    ball.className = `ball ${color}`;
    ball.style.left = `${x}px`;
    ball.style.top = `${y}px`;

    box.appendChild(ball);
}