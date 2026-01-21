// ================= DATA =================
const districtData = {
  Chennai: [
    {
      disease: "Dengue",
      dates: ["2026-01-01","2026-01-08","2026-01-15","2026-01-22","2026-01-29"],
      reported: [40,55,70,90,120],
      predicted: [140,160,180,200,220,240,260],
      risk: "High"
    },
    {
      disease: "Malaria",
      dates: ["2026-01-03","2026-01-10","2026-01-17","2026-01-24","2026-01-31"],
      reported: [20,25,30,35,40],
      predicted: [42,45,48,50,52,54,56],
      risk: "Medium"
    }
  ],
  Coimbatore: [
    {
      disease: "Influenza",
      dates: ["2026-01-02","2026-01-09","2026-01-16","2026-01-23","2026-01-30"],
      reported: [15,18,22,26,30],
      predicted: [32,35,38,40,42,44,46],
      risk: "Normal"
    }
  ]
};

// ================= ELEMENTS =================
const districtSelect = document.getElementById("districtSelect");
const diseaseFilter = document.getElementById("diseaseFilter");
const riskFilter = document.getElementById("riskFilter");
const fromDateInput = document.getElementById("fromDate");
const toDateInput = document.getElementById("toDate");
const tableBody = document.getElementById("diseaseTable");
const chartSection = document.getElementById("chartSection");
const chartTitle = document.getElementById("chartTitle");

let chartInstance = null;

// ================= RENDER TABLE =================
function renderTable(district) {
  tableBody.innerHTML = "";
  chartSection.style.display = "none";

  districtData[district].forEach((item, index) => {

    const latestDate = item.dates.at(-1);

    if (diseaseFilter.value && item.disease !== diseaseFilter.value) return;
    if (riskFilter.value && item.risk !== riskFilter.value) return;
    if (fromDateInput.value && latestDate < fromDateInput.value) return;
    if (toDateInput.value && latestDate > toDateInput.value) return;

    tableBody.innerHTML += `
      <tr>
        <td>${latestDate}</td>
        <td>${item.disease}</td>
        <td>${item.reported.at(-1)}</td>
        <td>${item.predicted.at(-1)}</td>
        <td>
          <span class="badge ${
            item.risk === "High" ? "bg-danger" :
            item.risk === "Medium" ? "bg-warning text-dark" : "bg-success"
          }">${item.risk}</span>
        </td>
        <td>
          <button class="btn btn-sm btn-outline-primary"
            onclick="showChart('${district}', ${index})">
            View
          </button>
        </td>
      </tr>
    `;
  });
}

// ================= DROPDOWN =================
districtSelect.addEventListener("change", () => {
  const district = districtSelect.value;
  if (!district) return;

  diseaseFilter.innerHTML = '<option value="">All</option>';
  districtData[district].forEach(item => {
    diseaseFilter.innerHTML += `<option value="${item.disease}">${item.disease}</option>`;
  });

  renderTable(district);
});

// ================= FILTER EVENTS =================
[diseaseFilter, riskFilter, fromDateInput, toDateInput].forEach(el => {
  el.addEventListener("change", () => {
    if (districtSelect.value) renderTable(districtSelect.value);
  });
});

// ================= CHART =================
function showChart(district, index) {
  const item = districtData[district][index];
  chartSection.style.display = "block";
  chartTitle.innerText = `${item.disease} – ${district}`;

  const labels = [
    "Week -4","Week -3","Week -2","Week -1","Current",
    "Day +1","Day +2","Day +3","Day +4","Day +5","Day +6","Day +7"
  ];

  const reportedLine = [
    ...item.reported,
    ...Array(7).fill(item.reported.at(-1))
  ];

  const predictedLine = [
    ...item.reported.slice(0,4),
    item.reported.at(-1),
    ...item.predicted
  ];

  if (chartInstance) chartInstance.destroy();

  chartInstance = new Chart(document.getElementById("trendChart"), {
    type: "line",
    data: {
      labels,
      datasets: [
        {
          label: "Reported Cases",
          data: reportedLine,
          borderColor: "#198754",
          tension: 0.35,
          pointRadius: 4
        },
        {
          label: "Predicted Cases",
          data: predictedLine,
          borderColor: "#dc3545",
          tension: 0.35,
          pointRadius: 4
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: "bottom" }
      },
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
}

// ================= MENU =================
function showSection(section) {
  ["dashboardSection","registerSection","pressSection"].forEach(id=>{
    document.getElementById(id).style.display="none";
  });
  document.getElementById(section+"Section").style.display="block";
}

// ================= LOGOUT =================
function logout() {
  window.location.href = "login.html";
}
