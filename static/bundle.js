'use strict';var three=require('three');const scene = new three.Scene();
const camera = new three.PerspectiveCamera( 70, window.innerWidth / window.innerHeight, 0.01, 10);
camera.position.z = 1;

geometry = new BoxGeometry( 0.2, 0.2, 0.2 );
material = new MeshNormalMaterial();

mesh = new THREE.Mesh( geometry, material );
const basic = basicScene();
scene.add( mesh );

const renderer = new three.WebGLRenderer({antialias: true});
renderer.setSize( window.innerWidth, window.innerHeight );

document.body.appendChild( renderer.domElement );

function animate() {
  requestAnimationFrame(animate);

  mesh.rotation.x += 0.01;
  mesh.rotation.y += 0.01;

  renderer.render( scene, camera );
}

animate();