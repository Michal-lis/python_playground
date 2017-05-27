// document.getElementById('get_persons').onclick = async () => {
//     res = await fetch("http://127.0.0.1:5000/persons", {method: "GET"});
//     if (res.ok) {
//         json = await res.json();
//         console.log(json)
//     } else {
//         console.error("error", res);
//     }
//     // fetch("http://127.0.0.1:5000/persons", {method: "GET"})
//     //     .catch(() => console.error("Fail zone"))
//     //     .then(res => {
//     //         if (res.ok) {
//     //             res.json().then(json => console.log(json));
//     //         }
//     //         else {
//     //             console.error("error", res);
//     //         }
//     //     });
// };


async function handler() {
    let res = await fetch("http://127.0.0.1:5000/persons", {method: "GET"});
    if (res.ok) {
        let json = await res.json();
        console.log(json)
    } else {
        console.error("error", res);
    }
}

document.getElementById('get_persons').onclick = handler;


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
