const follow_btn = document.querySelectorAll(".follow_btn");
const follow_btn1 = document.querySelector(".follow_btn1");
const counter = document.querySelector(".counter");
let count = 0;

follow_btn.forEach((each) => {
  each.addEventListener("click", () => {
    each.classList.toggle("active");

    if (each.classList.contains("active")) {
      each.textContent = "Following";
    } else {
      each.textContent = "Follow";
    }
  });
});

const checkbox = document.querySelector("#checkbox");
const toggle_btn = document.querySelector(".toggle");
const topics = document.querySelector(".topics");

checkbox.addEventListener("click", () => {
  topics.classList.toggle("active");
});
