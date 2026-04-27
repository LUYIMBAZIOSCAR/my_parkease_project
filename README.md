# Parkease

## Overview

Parkease is a web-based parking management system developed to help parking bay owners manage daily parking operations digitally and efficiently.

The system streamlines vehicle entry and exit processes, automates parking fee calculation, generates customer receipts, and provides administrative reporting tools. In addition to parking management, Parkease also includes digital management of tyre hire and battery hire services.

Parkease was developed as a full-stack web application using Django and SQLite.

---

## Problem Statement

Many parking bays still rely on manual record keeping, paper receipts, and inefficient tracking systems. This often leads to:

- Delays during vehicle entry and exit
- Poor financial accountability
- Difficulty tracking serviced vehicles
- Inefficient reporting
- Limited control over tyre and battery hire services

Parkease solves these challenges through automation and centralized digital management.

---

## Key Features

### Parking Management

- Register incoming vehicles at entry
- Record vehicle details digitally
- Automatic parking fee calculation on sign out
- Generate receipts with unique receipt numbers
- Track signed-out vehicles
- Improve speed and accuracy of operations

### Tyre Hire Management

- Record tyre hire services offered
- Dedicated tyre section manager
- Maintain service records

### Battery Hire Management

- Record battery hire services offered
- Dedicated battery section manager
- Maintain service records

### Administration

- Manage system users
- View parking activity reports
- View signed-out vehicle records
- Monitor tyre and battery service operations
- Full access dashboard for system administrator

---

## User Roles

### 1. Parking Attendant

Responsible for:

- Registering vehicles on arrival
- Managing sign out process
- Issuing customer receipts

### 2. Tyre Section Manager

Responsible for:

- Recording tyre hire services
- Managing tyre service records

### 3. Battery Section Manager

Responsible for:

- Recording battery hire services
- Managing battery service records

### 4. System Administrator

Responsible for:

- Managing users
- Viewing reports
- Monitoring all operations
- Reviewing signed-out vehicles

---

## System Workflow

1. Vehicle arrives at parking bay
2. Parking attendant registers vehicle into system
3. Vehicle remains parked
4. On departure, attendant signs out vehicle
5. System automatically calculates parking charges
6. Receipt generated with unique receipt number
7. Tyre or battery services (if requested) are recorded by respective managers
8. Administrator accesses reports and system data

---

## Technology Stack

### Frontend

- HTML
- CSS
- Bootstrap

### Backend

- Python
- Django Framework

### Database

- SQLite

---

## Benefits of Parkease

- Reduces manual paperwork
- Faster vehicle processing
- Accurate fee calculations
- Better accountability through receipts
- Centralized records management
- Improved reporting for owners
- Better service management for tyre and battery hire

---

## Future Improvements

- Online payment integration
- SMS/email receipt delivery
- QR code receipts
- Dashboard analytics
- Cloud deployment
- Mobile application
- Real-time parking slot availability

---

## Installation Guide

### Clone Repository

```bash
git clone https://github.com/yourusername/parkease.git
cd parkease
