document.getElementById('get_persons').onclick = () => {
    fetch("http://127.0.0.1:5000/persons", {method: "GET"})
        .catch(() => console.error("Fail zone"))
        .then(res => {
            if (res.ok) {
                res.json().then(json => console.log(json));
            }
            else {
                console.error("error", res);
            }
        });
};


// new Vue({
//     el: '#app',
//     data: {
//         message: 'Hello Vue.js!'
//     }
// })
//
// var foo = {
//     todos: [
//         {text: 'Learn JavaScript'},
//         {text: 'Learn Vue'},
//         {text: 'Build something awesome'}
//     ]
// }
//
// function foobar() {
//     fetch("http://127.0.0.1:5000/persons", {method: "GET"})
//         .catch(() => console.error("Fail zone"))
//         .then(res => {
//             if (res.ok) {
//                 res.json().then(json => console.log(json));
//             }
//             else {
//                 console.log("error", res);
//             }
//         });
// }
//
// var app4 = new Vue({
//     el: '#app-4',
//     data: foo
// })
