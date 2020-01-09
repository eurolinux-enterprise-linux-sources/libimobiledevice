/*
 * idevice.h
 * Device discovery and communication interface -- header file.
 *
 * Copyright (c) 2008 Zach C. All Rights Reserved.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 * 
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA 
 */
#ifndef IDEVICE_H
#define IDEVICE_H

#include <plist/plist.h>
#include <gnutls/gnutls.h>

#include "libimobiledevice/libimobiledevice.h"

enum connection_type {
	CONNECTION_USBMUXD = 1
};

struct ssl_data_int {
        gnutls_certificate_credentials_t certificate;
	gnutls_session_t session;
};
typedef struct ssl_data_int *ssl_data_t;

struct idevice_connection_int {
	enum connection_type type;
	void *data;
	ssl_data_t ssl_data;
};

struct idevice_int {
	char *uuid;
	enum connection_type conn_type;
	void *conn_data;
};

idevice_error_t idevice_connection_enable_ssl(idevice_connection_t connection);
idevice_error_t idevice_connection_disable_ssl(idevice_connection_t connection);

#endif
