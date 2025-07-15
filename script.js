// Handle Sign Up
function signIn() {
    const data = {
        user_first_name: document.getElementById("user_first_name").value,
        user_second_name: document.getElementById("user_second_name").value,
        user_surname: document.getElementById("user_surname").value,
        user_id_number: document.getElementById("user_id_number").value,
        user_email: document.getElementById("user_email").value,
        user_tel: document.getElementById("user_tel").value,
        user_password: document.getElementById("user_password").value
    };

    fetch("/sign_in", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            window.location.href = "/dashboard";
        } else {
            alert("Sign Up Failed: " + data.message);
        }
    })
    .catch(err => alert("Sign Up Failed: " + err));
}

// Handle Log In
function logIn() {
    const data = {
        user_email: document.getElementById("user_email").value,
        user_password: document.getElementById("user_password").value
    };

    fetch("/log_in", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            window.location.href = "/dashboard";
        } else {
            alert("Log In Failed: " + data.message);
        }
    })
    .catch(err => alert("Log In Failed: " + err));
}
