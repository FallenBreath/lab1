// gallery/static/gallery/js/viewer.js
import * as THREE from 'three';

export function mountSimpleCube(containerId) {
    const container = document.getElementById(containerId);
    if (!container) {
        console.error("Контейнер не найден:", containerId);
        return;
    }

    // Ждем, пока контейнер получит размеры
    setTimeout(() => {
        // --- А. СЦЕНА ---
        const scene = new THREE.Scene();
        scene.background = new THREE.Color(0xf0f0f0);

        // --- Б. КАМЕРА ---
        const width = container.clientWidth || 280; // запасной размер
        const height = container.clientHeight || 200;
        
        const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
        camera.position.z = 2;

        // --- В. РЕНДЕРЕР ---
        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(width, height);
        
        container.innerHTML = '';
        container.appendChild(renderer.domElement);

        // --- Г. ОБЪЕКТ (Куб) ---
        const geometry = new THREE.BoxGeometry(1, 1, 1);
        const material = new THREE.MeshStandardMaterial({ color: 0x007bff });
        const cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        // --- Д. СВЕТ ---
        const light = new THREE.DirectionalLight(0xffffff, 2);
        light.position.set(5, 5, 5);
        scene.add(light);
        
        const ambientLight = new THREE.AmbientLight(0x404040);
        scene.add(ambientLight);

        // --- Е. АНИМАЦИЯ ---
        function animate() {
            requestAnimationFrame(animate);
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;
            renderer.render(scene, camera);
        }
        animate();
        
        console.log("3D сцена запущена в", containerId);
    }, 100); // небольшая задержка для загрузки CSS
}