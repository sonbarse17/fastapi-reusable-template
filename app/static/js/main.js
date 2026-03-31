/**
 * FastAPI Starter – Client-Side JavaScript
 * =========================================
 * Handles micro-interactions and entrance animations.
 */

document.addEventListener("DOMContentLoaded", () => {
    // Staggered fade-in for feature cards
    const featureItems = document.querySelectorAll(".feature-item");
    featureItems.forEach((item, index) => {
        item.style.opacity = "0";
        item.style.transform = "translateY(20px)";
        item.style.transition = `opacity 0.5s ease ${index * 0.1}s, transform 0.5s ease ${index * 0.1}s`;

        // Trigger after a tiny delay so the browser registers the initial state
        requestAnimationFrame(() => {
            requestAnimationFrame(() => {
                item.style.opacity = "1";
                item.style.transform = "translateY(0)";
            });
        });
    });

    // Subtle parallax on blobs when mouse moves
    const blobs = document.querySelectorAll(".blob");
    document.addEventListener("mousemove", (e) => {
        const x = (e.clientX / window.innerWidth - 0.5) * 2;
        const y = (e.clientY / window.innerHeight - 0.5) * 2;
        blobs.forEach((blob, i) => {
            const speed = (i + 1) * 8;
            blob.style.transform = `translate(${x * speed}px, ${y * speed}px)`;
        });
    });
});
