// Reference data
const personalReferences = [
    {
        name: "Jhon Jairo Rivera Casado",
        position: "Líder del proyecto de bases de datos",
        company: "Tata Consultancy Services",
        phone: "321-489-8491"
    },
    {
        name: "Wiliam Alexander Useche Beltrán",
        position: "Administrador de bases de datos",
        company: "Tata Consultancy Services",
        phone: "301-700-4253"
    },
    {
        name: "Javier Alexander Lopera Carmona",
        position: "Administrador de bases de datos",
        company: "Tata Consultancy Services",
        phone: "319-686-5288"
    }
];

const familyReferences = [
    {
        name: "Yisela María Guzmán Morales",
        position: "Coordinadora Contable",
        company: "Innova Club S.A.S",
        phone: "320-507-44-25"
    },
    {
        name: "Lina María Calle Pérez",
        position: "Contadora",
        company: "Bruna Lingerie",
        phone: "315-616-50-80"
    }
];

// Function to create reference cards
function createReferenceCard(reference) {
    return `
        <div class="reference-card">
            <p><strong>Nombre:</strong> ${reference.name}</p>
            <p><strong>Cargo:</strong> ${reference.position}</p>
            <p><strong>Empresa:</strong> ${reference.company}</p>
            <p><strong>Teléfono:</strong> ${reference.phone}</p>
        </div>
    `;
}

// Populate references
document.addEventListener('DOMContentLoaded', () => {
    const personalReferencesContainer = document.getElementById('personalReferences');
    const familyReferencesContainer = document.getElementById('familyReferences');

    personalReferencesContainer.innerHTML = personalReferences
        .map(createReferenceCard)
        .join('');

    familyReferencesContainer.innerHTML = familyReferences
        .map(createReferenceCard)
        .join('');
});