# NanoBolt

NanoBolt is an easy-to-use, lightweight, and asynchronous Wi-Fi connectivity library for MicroPython-based devices. Developed primarily with a focus on the Raspberry Pi Pico W, NanoBolt aims to maintain compatibility with the ESP32 platform. 

The library provides a range of features from managing Wi-Fi connections and credentials to establishing a mock DNS server and a full asynchronous web server, all with an emphasis on being lightweight and memory-optimized for constrained devices.

## Table of Contents

* [Development Status](#development-status)
* [Motivation](#motivation)
* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Acknowledgements](#acknowledgements)
* [Disclaimer](#disclaimer)
* [License](#license)

## Development Status

**Pre-Alpha**

## Motivation

_This section will describe the motivation behind the creation of NanoBolt._

## Features

NanoBolt offers a range of features:

* **Connection Manager**: Effectively manages the Wi-Fi lifecycle, offering the following:
    * **Wi-Fi Connection**: Connects to a predefined Wi-Fi network using stored credentials.
    * **Access Point Mode**: In the absence of available credentials, the library starts an Access Point, enabling Wi-Fi configuration. This mode comes with several additional features:
        * **Mock DNS Server**: Acts as a captive portal, directing all DNS queries to the device's IP address to make the web interface easily accessible.
        * **REST APIs**: Provides a set of REST APIs to configure the Wi-Fi connection.
        * **Web Interface**: Exposes a simple and lightweight web interface for entering Wi-Fi credentials, which leverages the aforementioned APIs.

* **Asynchronous Web Server**: Implements a lightweight asynchronous web server, providing the necessary primitives to build simple web applications on MicroPython-based devices.

* **Bootstrap Code**: Offers an easy-to-use bootstrap code that initializes the Connection Manager and decides whether to connect to an available network or start the Access Point mode based on the availability of Wi-Fi credentials.

## Requirements
* [uasyncio](https://github.com/micropython/micropython-lib/tree/master/uasyncio) - micropython version of *async* library for big brother - python3.


## Installation

_Instructions for installing the NanoBolt library will go here._

## Usage

_Instructions for how to use the NanoBolt library will go here._

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how you can contribute to the development of NanoBolt.

## Acknowledgements

_This section will mention any significant contributions or inspirations._

## Disclaimer

_This section will outline any disclaimers associated with the use of the library._

## License

NanoBolt is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for more information.
