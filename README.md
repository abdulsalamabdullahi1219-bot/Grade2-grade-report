# Student Grade Performance Processing System (Modular Framework)
Course Code: COS102 — Introduction to Computer Science  
Program: Optometry

---

## Project Overview
This project is a modularized grade calculation system built using Python and the pandas library. Instead of using a single monolithic script, the system architecture splits the logic into independent code modules. These modules are integrated dynamically to extract data from James.csv and generate a centralized student performance summary.

---

## Group Members and Specific Contributions

* Abdulsalam Muhammed Awwal (25/55DZ011)
  * Contribution: Established the centralized repository workflow and structured the primary dataset layout (James.csv).

* Adefila James Adedamola (25/55DZ015)
  * Contribution: Programmed the module for extracting and processing English (ENG211) average metrics.

* Adabiri Olajesu Israel (25/55DZ014)
  * Contribution: Programmed the module for extracting and processing Chemistry (CHM213) average metrics.

* Adeniyi Abimifoluwa Opemipo (25/55DZ018)
  * Contribution: Authored the info.py module to handle project metadata and runtime configurations.

* Adeniyi Similoluwa Deborah (25/55DZ020)
  * Contribution: Programmed the module for extracting and processing Chemistry (CHM212) average metrics.

* Adekunle Suad Adeife (25/55DZ017)
  * Contribution: Engineered the master initialization script to link, load, and execute all external files.

* Adeniyi Aishat Oyinloye (25/55DZ019)
  * Contribution: Configured the core data science dependencies and environmental pandas library framework.

* Adekanye Halleluyah Toluwanimi (25/55DZ016)
  * Contribution: Programmed the module for extracting and processing General Studies (GST212) average metrics.

* Rodiat Abike Abdulrahmon (24/10AC045)
  * Contribution: Programmed the module for extracting and processing Optometry (OPT211) average metrics.

* Waliyyah Temitope Jimoh (24/46KA090)
  * Contribution: Authored the report_builder.py output script to format and compile calculations into report.txt.

* Abubakar Khadijah Ayomide (25/55DZ012)
  * Contribution: Compiled and organized the repository systems documentation and operational guidelines.

---

## Core System Features
* Modular Architecture: Individual course components run on isolated script modules to preserve clean code boundaries.
* Data Vectorization: Implements pandas-based optimization to execute aggregate computations seamlessly.
* Automated Logging: Generates and saves a polished text summary file for institutional records.
