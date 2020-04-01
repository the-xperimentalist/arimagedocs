
const form = document.querySelector("form")

form.addEventListener("submit", e => {
  e.preventDefault()

  const im = document.querySelector("#img").files[0]
  const m3d = document.querySelector("#m3d").files[0]

  console.log(im)
  console.log(document.querySelector("#img"))

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
