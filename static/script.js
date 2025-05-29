const labirinto = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1],
    [1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1],
    [1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,0,1],
    [1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,1],
    [1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1],
    [1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
];

const grid = document.getElementById("labirinto");
let inicio = null;
let fim = null;

// Criar grid com base no labirinto
labirinto.flat().forEach((_, idx) => {
  const row = Math.floor(idx / 21);
  const col = idx % 21;
  const cell = document.createElement("div");
  cell.className = "cell";
  cell.dataset.index = idx;

  if (labirinto[row][col] === 1) {
    cell.classList.add("parede");
  } else {
    cell.addEventListener("click", () => {
      if (!inicio) {
        inicio = idx;
        cell.classList.add("inicio");
      } else if (!fim && idx !== inicio) {
        fim = idx;
        cell.classList.add("fim");
      }
    });
  }

  grid.appendChild(cell);
});

// Botão de encontrar caminho
const btnEncontrar = document.getElementById("encontrar");
btnEncontrar.addEventListener("click", () => {
  if (inicio !== null && fim !== null) {
    fetch("/resolver", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ inicio, fim })
    })
    .then(res => res.json())
    .then(data => {
      if (data.caminho) {
        data.caminho.forEach(idx => {
          if (idx !== inicio && idx !== fim) {
            document.querySelector(`[data-index="${idx}"]`).classList.add("caminho");
          }
        });
      } else {
        alert("Nenhum caminho encontrado!");
      }
    });
  }
});

// Botão resetar
const btnResetar = document.getElementById("resetar");
btnResetar.addEventListener("click", () => {
  window.location.reload();
});
