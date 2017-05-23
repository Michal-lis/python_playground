new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue.js!'
    }
})

var foo = {
    todos: [
        {text: 'Learn JavaScript'},
        {text: 'Learn Vue'},
        {text: 'Build something awesome'}
    ]
}

// function foobar() {
//     fetch("http://127.0.0.1:5000/foo", {
//         method: "GET"
//     })
//         .catch(() => {
//             console.log("Fail zone");
//         }).then((res) => {
//         if (res.ok
//         ) {
//             res.json().then((json) => {
//                 return JSON.stringify(json, null, 2);
//             })
//             ;
//         }
//         else {
//             console.log("error", res);
//         }
//     })
//     ;
// }

var app4 = new Vue({
    el: '#app-4',
    data: foo
})
