
const socket = io('http://192.168.68.112:80');



document.getElementById('tempToggle').addEventListener('change', function () {
    const switchState = this.checked ? 1 : 0;
    socket.emit('switch_state', {switch: switchState});

});

socket.on('new_data', (data) => {
    console.log('New data received:', data);
    document.querySelector(".humidity").innerHTML = data.hamuduty + "%";
    document.querySelector(".temp").innerHTML = Math.round(data.temperatura) + "°C";
});



socket.on('new_data', (data) => {
    console.log('New data received:', data);
    document.querySelector(".humidity").innerHTML = data.hamuduty + "%";
    document.querySelector(".temp").innerHTML = Math.round(data.temperatura) + "°C";
});

