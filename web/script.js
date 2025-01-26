document.addEventListener('DOMContentLoaded', () => {
    const simpleModeBtn = document.getElementById('simple-mode-btn');
    const advancedModeBtn = document.getElementById('advanced-mode-btn');
    const modelsBtn = document.getElementById('models-btn');

    const simpleMode = document.getElementById('simple-mode');
    const advancedMode = document.getElementById('advanced-mode');
    const modelsSection = document.getElementById('models-section');
    const modeSelectorSection = document.querySelector('.mode-selector');

    const modelSelect = document.getElementById('model-select');

    // Mode Switching
    function showSection(section) {
        [simpleMode, advancedMode, modelsSection].forEach(s => s.classList.add('hidden'));
        modeSelectorSection.style.display = 'none';
        section.classList.remove('hidden');
    }

    function returnToMainMenu() {
        // Hide all mode sections
        [simpleMode, advancedMode, modelsSection].forEach(s => s.classList.add('hidden'));
        
        // Show mode selector buttons
        modeSelectorSection.style.display = 'flex';

        // Clear inputs and responses
        document.getElementById('simple-prompt').value = '';
        document.getElementById('simple-response').textContent = '';
        document.getElementById('advanced-prompt').value = '';
        document.getElementById('system-prompt').value = '';
        document.getElementById('advanced-response').textContent = '';
    }

    // Add return to main menu buttons to each section
    const returnButtons = document.querySelectorAll('.return-main-menu');
    returnButtons.forEach(btn => {
        btn.addEventListener('click', returnToMainMenu);
    });

    // Simple Mode Submit
    const simpleSubmitBtn = document.getElementById('simple-submit');
    if (simpleSubmitBtn) {
        simpleSubmitBtn.addEventListener('click', () => {
            const prompt = document.getElementById('simple-prompt').value;
            const responseArea = document.getElementById('simple-response');
            
            if (prompt.trim()) {
                responseArea.textContent = 'Processing...';
                eel.run_simple_mode(prompt)((response) => {
                    responseArea.textContent = response;
                });
            }
        });
    }

    // Advanced Mode Submit
    const advancedSubmitBtn = document.getElementById('advanced-submit');
    if (advancedSubmitBtn) {
        advancedSubmitBtn.addEventListener('click', () => {
            const selectedModel = document.getElementById('model-select').value;
            const systemPrompt = document.getElementById('system-prompt').value;
            const prompt = document.getElementById('advanced-prompt').value;
            const responseArea = document.getElementById('advanced-response');
            
            if (prompt.trim()) {
                responseArea.textContent = 'Processing...';
                eel.run_advanced_mode(selectedModel, systemPrompt, prompt)((response) => {
                    responseArea.textContent = response;
                });
            }
        });
    }

    simpleModeBtn.addEventListener('click', () => showSection(simpleMode));
    advancedModeBtn.addEventListener('click', () => {
        showSection(advancedMode);
        // Populate models if not already populated
        if (modelSelect.children.length === 0) {
            eel.get_available_models()((models) => {
                models.forEach(model => {
                    const option = document.createElement('option');
                    option.value = model;
                    option.textContent = model;
                    modelSelect.appendChild(option);
                });
            });
        }
    });
    modelsBtn.addEventListener('click', () => {
        showSection(modelsSection);
        eel.get_available_models()((models) => {
            const modelsList = document.getElementById('models-list');
            modelsList.innerHTML = models.map(model => `<p>${model}</p>`).join('');
        });
    });
});
