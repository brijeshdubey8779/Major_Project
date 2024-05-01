// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract DoctorRegistry {
    // Define a struct to represent doctor information
    struct Doctor {
        uint id;
        string name;
        string specialization;
        address walletAddress; // Address of the doctor's Ethereum wallet
        // Add more fields as needed
    }

    // Mapping to store doctor information using doctor ID
    mapping(uint => Doctor) public doctors;

    // Event to log doctor registration
    event DoctorRegistered(uint id, string name, string specialization, address walletAddress);

    // Function to register a new doctor
    function registerDoctor(uint _id, string memory _name, string memory _specialization, address _walletAddress) public {
        // Create a new Doctor struct
        Doctor memory newDoctor = Doctor(_id, _name, _specialization, _walletAddress);
        // Store doctor information in the mapping
        doctors[_id] = newDoctor;
        // Emit an event to log the registration of the doctor
        emit DoctorRegistered(_id, _name, _specialization, _walletAddress);
    }

    // Function to get doctor information by ID
    function getDoctor(uint _id) public view returns (uint, string memory, string memory, address) {
        // Return doctor information from the mapping
        return (doctors[_id].id, doctors[_id].name, doctors[_id].specialization, doctors[_id].walletAddress);
    }
}
