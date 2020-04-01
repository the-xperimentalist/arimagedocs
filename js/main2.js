
const form = document.querySelector("form")

form.addEventListener("submit", e => {
  e.preventDefault()

  const im = document.querySelector("#img").file
  const m3d = document.querySelector("#3d").file

  const formData = new FormData()
  formData.append("temp_img", im)
  formData.append("model_3d", m3d)

  fetch("http://localhost:5000/add_img_temp/", {
    method: "POST",
    body: formData
  }).then(res => {
    alert("Added template")
  })
})
