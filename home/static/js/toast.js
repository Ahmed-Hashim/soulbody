(function () {
  const toastElement = document.getElementById("toast");
  const toastBody = document.getElementById("toast-body");

  const toast = new bootstrap.Toast(toastElement, { delay: 2000 });
  htmx.on("type", (e) => {
    toastElement.classList.remove("bg-primary");
    toastElement.classList.remove("bg-secondary");
    toastElement.classList.remove("bg-success");
    toastElement.classList.remove("bg-danger");
    toastElement.classList.remove("bg-warning");
    toastElement.classList.remove("bg-info");
    toastElement.classList.remove("bg-light");
    toastElement.classList.remove("bg-dark");
    toastElement.classList.add(e.detail.value);
  });
  htmx.on("showMessage", (e) => {
    console.log(e.detail.value)
    toastBody.innerText = e.detail.value;
    toast.show();
  });
})();


