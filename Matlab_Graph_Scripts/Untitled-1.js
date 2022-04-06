

const targetNode = document.getElementById('remote-video-wrapper');
const config = { attributes: true, childList: false, subtree: false };
new MutationObserver(function(mutationsList, observer) {
    for(const mutation of mutationsList) {
        if  (mutation.type === 'attributes' && mutation.attributeName === 'class'){
            targetNode.style.filter="blur(20px)"
        }
    }
}).observe(targetNode, config);
document.addEventListener('keydown', function(event) {
    if (event.ctrlKey && event.key === 'y') {
        targetNode.style.filter="";
    }
  });


observer.disconnect();



backdrop-filter: blur(6px);

filter:blur(4px);
    -o-filter:blur(4px);
    -ms-filter:blur(4px);
    -moz-filter:blur(4px);
    -webkit-filter:blur(4px);