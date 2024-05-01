// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract PatientData {
    // Define a struct to represent patient data
    struct Patient {
        uint256 id;
        string name;
        uint256 age;
        string diagnosis;
        // Add more fields as needed
    }

    // Mapping to store patient data using patient ID
    mapping(uint256 => Patient) public patients;

    // Event to log patient data creation
    event PatientCreated(
        uint256 id,
        string name,
        uint256 age,
        string diagnosis
    );

    // Function to add patient data to the contract
    function addPatient(
        uint256 _id,
        string memory _name,
        uint256 _age,
        string memory _diagnosis
    ) public {
        // Create a new Patient struct
        Patient memory newPatient = Patient(_id, _name, _age, _diagnosis);
        // Store patient data in the mapping
        patients[_id] = newPatient;
        // Emit an event to log the creation of patient data
        emit PatientCreated(_id, _name, _age, _diagnosis);
    }

    // Function to get patient data by ID
    function getPatient(
        uint256 _id
    ) public view returns (uint256, string memory, uint256, string memory) {
        // Return patient data from the mapping
        return (
            patients[_id].id,
            patients[_id].name,
            patients[_id].age,
            patients[_id].diagnosis
        );
    }
}
