const ctx_company_a = document.getElementById('company-a');
const ctx_company_b = document.getElementById('company-b');

new Chart(ctx_company_a, {
  type: 'doughnut',
  data: {
    labels: [
      'return 200% prob 50%',
      'return 0% prob 50%',
    ],
    datasets: [{
      label: 'Prospek A',
      data: [50, 50],
      backgroundColor: [
        'rgb(255, 99, 132)', // Red
        'rgb(54, 162, 235)', // Blue
        // 'rgb(255, 205, 86)' // Yellow
      ],
      hoverOffset: 4
    }]
  },
});
new Chart(ctx_company_b, {
  type: 'doughnut',
  data: {
    labels: [
      'return 150% prob 75%',
      'return 0% prob 25%',
    ],
    datasets: [{
      label: 'Prospek B',
      data: [75, 25],
      backgroundColor: [
        'rgb(255, 99, 132)', // Red
        'rgb(54, 162, 235)', // Blue
        // 'rgb(255, 205, 86)' // Yellow
      ],
      hoverOffset: 4
    }]
  },
});