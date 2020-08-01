let ipt = document.querySelector('input');
let btn = document.querySelector('button');
let elem = document.querySelector('p');

btn.addEventListener('click', () => {
  elem.innerText = ipt.value;
} );
