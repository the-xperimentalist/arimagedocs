// Set constraints for the video stream
var constraints = { video: { facingMode: "user" }, audio: false };



var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );

var renderer = new THREE.WebGLRenderer({ alpha: true });
renderer.setClearAlpha(0.0);
renderer.setSize( window.innerWidth, window.innerHeight );
// document.body.appendChild( renderer.domElement );

var geometry = new THREE.BoxGeometry( 20, 20, 20);
var material = new THREE.MeshLambertMaterial( { color: 0xfd59d7 } );
var cube = new THREE.Mesh( geometry, material );
scene.add( cube );

for (var i = 0, l = geometry.vertices.length; i<l; i++) {
    geometry.vertices[i].x += -10 + Math.random()*20
    geometry.vertices[i].y += -10 + Math.random()*20
}

cube.rotation.x = 0.45
cube.rotation.y = -0.25

camera.position.z = 100

var light = new THREE.PointLight( 0xFFFF00 )
light.position.set( 10, 0, 25 )
scene.add( light )

var render = function () {
    requestAnimationFrame( render )
    cube.rotation.x += 0.05
    renderer.render( scene, camera)
}


// Define constants
const cameraView = document.querySelector("#camera--view"),
    cameraOutput = document.querySelector("#camera--output"),
    cameraSensor = document.querySelector("#camera--sensor"),
    cameraTrigger = document.querySelector("#camera--trigger")
// Access the device camera and stream to cameraView

// makeblob = function (dataURL) {
//             var BASE64_MARKER = ';base64,';
//             if (dataURL.indexOf(BASE64_MARKER) == -1) {
//                 var parts = dataURL.split(',');
//                 var contentType = parts[0].split(':')[1];
//                 var raw = decodeURIComponent(parts[1]);
//                 return new Blob([raw], { type: contentType });
//             }
//             var parts = dataURL.split(BASE64_MARKER);
//             var contentType = parts[0].split(':')[1];
//             var raw = window.atob(parts[1]);
//             var rawLength = raw.length;

//             var uInt8Array = new Uint8Array(rawLength);

//             for (var i = 0; i < rawLength; ++i) {
//                 uInt8Array[i] = raw.charCodeAt(i);
//             }

//             return new Blob([uInt8Array], { type: contentType });
//         }

function initEarth () {}


function cameraStart() {
    navigator.mediaDevices
        .getUserMedia(constraints)
        .then(function(stream) {
        track = stream.getTracks()[0];
        cameraView.srcObject = stream;
    })
    .catch(function(error) {
        console.error("Oops. Something is broken.", error);
    });
}

// Take a picture when cameraTrigger is tapped
cameraTrigger.onclick = function() {
    cameraSensor.width = cameraView.videoWidth;
    cameraSensor.height = cameraView.videoHeight;
    cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
    cameraOutput.src = cameraSensor.toDataURL();
    cameraOutput.classList.add("taken");

    console.log(document.location.href)

    // console.log(cameraOutput)
    // console.log(cameraOutput.src)

    const im = cameraOutput.src
    const formData = new FormData();
    // console.log(im)
    // formData.append("asas", "hjcsjas")
    // formData.append("img", im)
    // console.log(formData)

    console.log(im)
    // console.log(formData)

    // const data = {"img": "Assaas"}
    // console.log(data)
    // console.log(typeof im)

    // Canvas2Image.saveAsJPEG(im)
    // document.location.href = im.replace("image/png", 'image/octet-stream');

    fetch("http://localhost:5000/temp_detect/", {
      method: "POST",
      body: JSON.stringify({"img": im}),
      headers: {
        "Content-Type": "application/json"
      }
    }).then(res => {
        console.log("Done")
        // document.querySelector("main").style.display = "none"
        document.querySelector("canvas#camera--sensor").classList.add("cls-less")
        document.querySelector("button#camera--trigger").classList.add("higher-btn")
        renderer.domElement.classList.add("cls")
        document.querySelector("main").appendChild(renderer.domElement)
        // document.body.appendChild( renderer.domElement );
        // document.querySelector("canvas").style.display = "block"
        render()
    })
};
// Start the video stream when the window loads
window.addEventListener("load", cameraStart, false);
