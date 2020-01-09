/**
 * @file libimobiledevice/mobilesync.h
 * @brief MobileSync Implementation
 * \internal
 *
 * Copyright (c) 2009 Jonathan Beck All Rights Reserved.
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

#ifndef IMOBILESYNC_H
#define IMOBILESYNC_H

#ifdef __cplusplus
extern "C" {
#endif

#include <libimobiledevice/libimobiledevice.h>

/* Error Codes */
#define MOBILESYNC_E_SUCCESS                0
#define MOBILESYNC_E_INVALID_ARG           -1
#define MOBILESYNC_E_PLIST_ERROR           -2
#define MOBILESYNC_E_MUX_ERROR             -3
#define MOBILESYNC_E_BAD_VERSION           -4

#define MOBILESYNC_E_UNKNOWN_ERROR       -256

typedef int16_t mobilesync_error_t;

struct mobilesync_client_int;
typedef struct mobilesync_client_int *mobilesync_client_t;

mobilesync_error_t mobilesync_client_new(idevice_t device, uint16_t port, mobilesync_client_t * client);
mobilesync_error_t mobilesync_client_free(mobilesync_client_t client);
mobilesync_error_t mobilesync_receive(mobilesync_client_t client, plist_t *plist);
mobilesync_error_t mobilesync_send(mobilesync_client_t client, plist_t plist);

#ifdef __cplusplus
}
#endif

#endif
