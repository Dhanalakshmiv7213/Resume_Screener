async function analyzeResume() {

    const fileInput = document.getElementById("resumeFile");
    const jobDescription = document.getElementById("jobDescription").value;

    if (!fileInput.files[0]) {
        alert("Please upload a resume PDF");
        return;
    }

    const formData = new FormData();

    formData.append("file", fileInput.files[0]);
    formData.append("job_description", jobDescription);
    document.querySelector("button").innerText = "Analyzing...";
    try {

        const response = await fetch(
            "http://127.0.0.1:8000/analyze",
            {
                method: "POST",
                body: formData
            }
        );
        
        const data = await response.json();

        document.getElementById("resultCard").style.display = "block";

        document.getElementById("filename").innerText =
            data.filename;

        document.getElementById("skills").innerText =
            data.skills.join(", ");

        document.getElementById("score").innerText =
            data.match_score;
        document.querySelector("button").innerText = "Analyze Resume";
    } catch (error) {

        console.error(error);

        alert("Error analyzing resume");

    }
}