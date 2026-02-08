const ctx_risk_a = document.getElementById('risk-a');
const ctx_risk_b = document.getElementById('risk-b');

new Chart(ctx_risk_a, {
  type: 'doughnut',
  data: {
    labels: [
      '200 token prob 5%',
      '150 token prob 90%',
      '0 token prob 5%'
    ],
    datasets: [{
      label: 'Prospek A',
      data: [5, 90, 5],
      backgroundColor: [
        'rgb(255, 99, 132)', // Red
        'rgb(54, 162, 235)', // Blue
        'rgb(255, 205, 86)' // Yellow
      ],
      hoverOffset: 4
    }]
  },
});
new Chart(ctx_risk_b, {
  type: 'doughnut',
  data: {
    labels: [
      '180 token prob 5%',
      '150 token prob 90%',
      '0 token prob 5%'
    ],
    datasets: [{
      label: 'Prospek B',
      data: [5, 90, 5],
      backgroundColor: [
        'rgb(255, 99, 132)', // Red
        'rgb(54, 162, 235)', // Blue
        'rgb(255, 205, 86)' // Yellow
      ],
      hoverOffset: 4
    }]
  },
});