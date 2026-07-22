const analyzeBtn = document.getElementById("analyzeBtn");

const loading = document.getElementById("loading");
const result = document.getElementById("result");

analyzeBtn.addEventListener("click", async () => {

    const file = document.getElementById("resume").files[0];

    const jobDescription =
        document.getElementById("jobDescription").value;

    if (!file) {
        alert("Please upload a PDF Resume.");
        return;
    }

    loading.style.display = "block";
    result.style.display = "none";

    const formData = new FormData();

    formData.append("file", file);
    formData.append("job_description", jobDescription);

    try {

        const response = await fetch(
            "/analyze",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        loading.style.display = "none";
        result.style.display = "block";

        if (!data.success) {

            alert(data.error);
            return;

        }

        const analysis = data.analysis;

        function section(start, end) {

            const startIndex = analysis.indexOf(start);

            if (startIndex === -1)
                return "Not Available";

            let finish;

            if (end === "") {

                finish = analysis.length;

            } else {

                finish = analysis.indexOf(end);

                if (finish === -1)
                    finish = analysis.length;
            }

            return analysis.substring(
                startIndex + start.length,
                finish
            ).trim();

        }

        document.getElementById("atsScore").innerHTML =
            section("ATS Score:", "Professional Summary:");

        document.getElementById("summary").innerHTML =
            section("Professional Summary:", "Strengths:");

        document.getElementById("strengths").innerHTML =
            section("Strengths:", "Weaknesses:");

        document.getElementById("weaknesses").innerHTML =
            section("Weaknesses:", "Missing Skills:");

        document.getElementById("missingSkills").innerHTML =
            section("Missing Skills:", "Grammar Suggestions:");

        document.getElementById("jobRoles").innerHTML =
            section("Best Job Roles:", "Resume Improvement Tips:");

        document.getElementById("tips").innerHTML =
            section("Resume Improvement Tips:", "Final Verdict:");

        document.getElementById("verdict").innerHTML =
            section("Final Verdict:", "");

    }

    catch (error) {

        loading.style.display = "none";

        alert("Unable to connect to backend.");

    }

});